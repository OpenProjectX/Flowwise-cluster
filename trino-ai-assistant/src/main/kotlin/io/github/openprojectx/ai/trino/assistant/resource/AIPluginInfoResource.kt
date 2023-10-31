package io.github.openprojectx.ai.trino.assistant.resource

import io.github.openprojectx.ai.trino.assistant.domain.AIPluginInfo
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RestController

@RestController
class AIPluginInfoResource {

    @GetMapping("/.well-known/ai-plugin.json")
    fun aiPluginInfo(): AIPluginInfo {
        return AIPluginInfo()
    }
}